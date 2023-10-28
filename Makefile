SERVICE_NAME=sample-app

default: run

help:
	@echo "⚈ build			---> 🏗️ Build project via Docker Build."
	@echo "⚈ run			---> 🎮 Run project via Docker Run."
	@echo "⚈ rund			---> 🎮 Run project locally in detach mode."
	@echo "⚈ logs			---> 📜 Show logging stream for project."

build:
	@echo "\n> 🏗️ [Build] Building $(SERVICE_NAME) via Docker Build...\n"
	docker build -t $(SERVICE_NAME) .

run: build
	@echo "\n> 🎮 [Run] Running $(SERVICE_NAME) via Docker Run...\n"
	docker run -p 9090:8080 $(SERVICE_NAME)

rund:
	@echo "\n> 🎮 [Detach] Starting $(SERVICE_NAME) via Docker Compose in detach mode...\n"
	docker-compose up -d --force-recreate --build

logs:
	@echo "\n> 📜 Showing App logs...\n"
	docker-compose logs -f