package main

import (
	"example/workout_api_golang/internal/controllers"
	"example/workout_api_golang/internal/database"
	"example/workout_api_golang/internal/models"
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	loadEnv()
	loadDatabase()
	serveApplication()
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

func serveApplication() {
	router := gin.Default()

	publicRoutes := router.Group("/users")
	publicRoutes.POST("/", controllers.AddUser)
	publicRoutes.GET("/:nickname", controllers.GetUser)
	publicRoutes.PUT("/:nickname", controllers.UpdateUser)

	router.Run(":8000")
	fmt.Println("Server is running on port 8000")
}
