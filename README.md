Приложение, которое по REST API сервиса OnCall создает команды/сотрудников команд и их дежурства согласно следующему описанию:

```
---
teams:
  - name: "k8s SRE"
    scheduling_timezone: "Europe/Moscow"
    email: "k8s@sre-course.ru"
    slack_channel: "#k8s-team"
    users:
      - name: "o.ivanov"
        full_name: "Oleg Ivanov"
        phone_number: "+1 111-111-1111"
        email: "o.ivanov@sre-course.ru"
        duty:
          - date: "02/10/2023"
            role: "primary"
          - date: "03/10/2023"
            role: "secondary"
          - date: "04/10/2023"
            role: "primary"
          - date: "05/10/2023"
            role: "secondary"
          - date: "06/10/2023"
            role: "primary"
      - name: "d.petrov"
        full_name: "Dmitriy Petrov"
        phone_number: "+1 211-111-1111"
        email: "d.petrov@sre-course.ru"
        duty:
          - date: "02/10/2023"
            role: "secondary"
          - date: "03/10/2023"
            role: "primary"
          - date: "04/10/2023"
            role: "secondary"
          - date: "05/10/2023"
            role: "primary"
          - date: "06/10/2023"
            role: "secondary"

  - name: "DBA SRE"
    scheduling_timezone: "Asia/Novosibirsk"
    email: "dba@sre-course.ru"
    slack_channel: "#dba-team"
    users:
      - name: "a.seledkov"
        full_name: "Alexander Seledkov"
        phone_number: "+1 311-111-1111"
        email: "a.seledkov@sre-course.ru"
        duty:
          - date: "02/10/2023"
            role: "primary"
          - date: "03/10/2023"
            role: "primary"
          - date: "04/10/2023"
            role: "primary"
          - date: "05/10/2023"
            role: "secondary"
          - date: "06/10/2023"
            role: "primary"
      - name: "d.hludeev"
        full_name: "Dmitriy Hludeev"
        phone_number: "+1 411-111-1111"
        email: "user-4@sre-course.ru"
        duty:
          - date: "02/10/2023"
            role: "secondary"
          - date: "03/10/2023"
            role: "secondary"
          - date: "04/10/2023"
            role: "vacation"
          - date: "05/10/2023"
            role: "primary"
          - date: "06/10/2023"
            role: "secondary"
```

Запуск приложения: ```docker compose up```
