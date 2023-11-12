package controllers

import (
	"example/workout_api_golang/internal/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func AddUser(context *gin.Context) {
	var input models.User
	if err := context.ShouldBindJSON(&input); err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newUser := &models.User{
		Nickname: input.Nickname,
		Name:     input.Name,
		Surname:  input.Surname,
		Email:    input.Email,
		Height:   input.Height,
		Joined:   input.Joined,
	}

	createdUser, err := newUser.Create()
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": "Failed to create user"})
		return
	}

	context.JSON(http.StatusOK, createdUser)
}

func GetUser(context *gin.Context) {
	nickname := context.Param("nickname")
	user, err := models.Find(nickname)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
		return
	}

	context.JSON(http.StatusOK, user)
}

func UpdateUser(context *gin.Context) {
	nickname := context.Param("nickname")
	user, err := models.Find(nickname)
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
		return
	}

	var input models.User
	if err := context.ShouldBindJSON(&input); err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	// TODO: Dont change values to empty if not provided
	user.Name = input.Name
	user.Surname = input.Surname
	user.Email = input.Email
	user.Height = input.Height
	user.Joined = input.Joined

	updatedUser, err := user.Update()
	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{"error": "Failed to update user"})
		return
	}

	context.JSON(http.StatusOK, updatedUser)
}
