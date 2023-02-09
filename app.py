import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

def generate_text(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def main():
    st.title("2023年运势生成器")
    model = "text-davinci-003"
    name = st.text_input("请输入您的名字")
    born = st.text_input("请输入你的出生年月日")
    description = st.text_input("请描述您的具体需求")
    length = st.selectbox("选择生成内容的字数", [100, 200, 300, 400, 500])
    prompt = f"生成{born}出生的 {name} 2023年运势：{description}"

    if st.button("生成运势"):
        prediction = generate_text(model, prompt)
        prediction = prediction[:length]
        st.write("生成的运势：", prediction)
        st.write("将生成的内容保存到您的设备：")
        st.text_area("", prediction, height=300)

if __name__ == "__main__":
    main()

