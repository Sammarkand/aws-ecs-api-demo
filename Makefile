ECR_A ?=
ECR_B ?=

build:
\tdocker build -t service-a:local ./service-a
\tdocker build -t service-b:local ./service-b

push:
\tdocker tag service-a:local $(ECR_A):latest && docker push $(ECR_A):latest
\tdocker tag service-b:local $(ECR_B):latest && docker push $(ECR_B):latest

up:
\tdocker compose up --build

down:
\tdocker compose down -v
