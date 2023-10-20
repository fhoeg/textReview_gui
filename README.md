# Text review assistant
example for a tool that helps improving texts based on given guidelines. This tool is used for an internal demo but may be a basis for a real usecase.

The idea is to make life easier for content writers without taking all responsibility away from them. It only helps to ensure a consistently high quality in content creation.

The file "system.txt" may serve as an example. It is in German.

Within the app you could upload any txt file and therefore define any kind of assistant. Keep in mind that the max tokens are shared between prompt, resonse and system role so the txt file should be as brief as possible. In a future version I might look into experimenting with text splitting and vector search for more complex guidelines.

## How-to
1. Clone the repo
2. Create an API key on [platform.openai.com](https://platform.openai.com/account/api-keys)https://platform.openai.com/account/api-keys
3. create <code>.env</code> in your main folder, copy the content from <code>.env.example</code> and then paste your openai API key which you just created
4. Create a virtual environment and activate it
5. run <code>pip install -r requirements.txt</code>
6. start the app by running <code>streamlit run app.py</code>
