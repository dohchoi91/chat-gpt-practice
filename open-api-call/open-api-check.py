import openai

openai.api_key = ""
# database = ""

def chat(message, database=""):

  print("database : {}".format(database))

  response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": database},
          {"role": "user", "content": message},
      ]
  )
  print(response.choices[0]["message"]["content"])



def main():
  chat("안녕")
  chat("한화생명 IT운영팀 최동현에서 대해서 알려줘")

  database = "한화생명 최동현은 2023년에 경력직으로 입사해서 스마트플래너 개발, 운영업무를 담당하고 있음."
  chat("한화생명 최동현에 대해서 알려줘.", database)



if __name__ == "__main__":
    main()