default: rund logs

help:
	@echo "⚈ rund			---> 🎮 Run project locally in detach mode."
	@echo "⚈ logs			---> 📜 Show logging stream for project."
	
rund:
	@echo "\n> 🎮 [Detach] Starting ${GCP_SERVICE_NAME} via Docker Compose in detach mode...\n"
	docker-compose up -d

logs:
	@echo "\n> 📜 Showing App logs...\n"
	docker-compose logs -f