from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret import openai_key
import os
os.environ['OPENAI_API_KEY'] = openai_key

llm = OpenAI(temperature=0.6, max_tokens=350)


def generate_story(name, genre):

    # formatting the prompt
    story_prompt = PromptTemplate(
        input_variables=["name", "genre"],
        template="Write a short story strictly within 300 words with {name} as the main character and {genre} as the genre of the story.The story should have a clear beginning, middle, and resolution. Focus on building tension and creating a satisfying conclusion.",
    )

    # generating the story chain with the prompt
    story_chain = LLMChain(llm=llm, prompt=story_prompt, output_key='story')

    # generating the sequential chain
    chain = SequentialChain(
        chains=[story_chain],
        input_variables=['name', 'genre'],
        output_variables=['story']
    )

    # generating the story by running the sequential chain
    story = chain({'name': name, 'genre': genre})

    return story


if __name__ == "__main__":
    out = generate_story("Yogesh", "romantic")
    print(out['story'])
