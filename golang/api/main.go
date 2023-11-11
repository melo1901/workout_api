package main

import (
	"example/workout_api_golang/internal/database"
	models "example/workout_api_golang/internal/models"
	"log"

	"github.com/joho/godotenv"
)

func main() {
	loadEnv()
	loadDatabase()
}

func loadDatabase() {
	database.Connect()
	database.DB.AutoMigrate(&models.User{}, &models.Health{}, &models.Activity{})
}

func loadEnv() {
	err := godotenv.Load(".env")

	if err != nil {
		log.Fatalf("Error loading .env file")
	}
}
