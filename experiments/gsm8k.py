# Portions of this code are
# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import copy
import json
import argparse
import concurrent.futures


from langchain.chains import PALGenericChain, PALChain
from langchain.vectorstores import Chroma
import lessons

from langchain import OpenAI
import os

parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true', default=True)
parser.add_argument('--verbose', action='store_true', default=True)
parser.add_argument('--dataset', default='gsm8k', type=str)
parser.add_argument('--model', default='gpt-3.5-turbo-0613', type=str)
parser.add_argument('--majority_at', default=None, type=int)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=2048, type=int)
parser.add_argument('--mode', default='pal', type=str)
parser.add_argument('--workers', default=4, type=int)

args = parser.parse_args()

DATA_PATH = f'{args.dataset}.jsonl'
OUTPUT_PATH = f'{args.mode}_{args.model}_{args.dataset}_results.jsonl'

examples = list(map(json.loads, open(DATA_PATH)))


os.environ['OPENAI_API_KEY'] = 'sk-sHdd3jVAqyCPEiShN8sOT3B' + 'lbkFJMGaOoCiZGt77yUyJ3Ye4'

llm = OpenAI(temperature=args.temperature, max_tokens=args.max_tokens, model_name=args.model)
if args.mode == 'palgeneric':
    from langchain.embeddings.openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
    vectorstore=Chroma
    chain = PALGenericChain.from_generic_prompt(llm, embeddings, vectorstore, lessons.lessons, verbose=True)
    pass
elif args.mode == 'pal':
    chain = PALChain.from_math_prompt(llm, verbose=args.verbose)
else:
    raise NotImplementedError(f'unimplemented mode {args.mode}')


if args.append:
    try:
        lines = open(OUTPUT_PATH).readlines()
        scores = [x['score'] for x in map(json.loads, lines)]
        already_completed = [x['input'] for x in map(json.loads, lines)]
    except FileNotFoundError:
        scores = []

else:
    scores = []

def process(x):
    question = x['input']
    result = copy.copy(x)

    try:
        ans = chain.run(question=question)
        ans = float(ans)
        score = 1 if abs(ans - x['target']) < 1e-3 else 0
    except Exception as e:
        print(x, e)
        ans = ''
        score = 0


    result['answer'] = ans
    result['score'] = score
    return result


# Zap file if we are not in append mode
if not args.append:
    with open(OUTPUT_PATH, 'w') as f:
        f.flush()

with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:

    future_to_work = {executor.submit(process, x): x for x in examples if x['input'] not in already_completed}

    for future in concurrent.futures.as_completed(future_to_work):
        work = future_to_work[future]
        try:
            result = future.result()
            scores.append(result['score'])

            with open(OUTPUT_PATH, 'a') as f:
                f.write(json.dumps(result) + '\n')
                f.flush()
        except Exception as e:
            print(f'job {work} created an exception : {e}')

        print(f'Accuracy so far - {sum(scores) / len(scores)} on {len(scores)} of {len(examples)}')


print(f'Accuracy - {sum(scores) / len(scores)}')