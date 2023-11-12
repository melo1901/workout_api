package models

import (
	"example/workout_api_golang/internal/database"
	"html"
	"strings"

	"gorm.io/gorm"
)

type User struct {
	Nickname      string     `gorm:"primaryKey;size:255;unique;not null" json:"nickname"`
	Name          string     `gorm:"size:255;not null" json:"name"`
	Surname       string     `gorm:"size:255;not null" json:"surname"`
	Email         string     `gorm:"size:255;unique;not null" json:"email"`
	Height        float32    `json:"height"`
	Joined        string     `gorm:"not null" json:"joined"`
	HealthHistory []Health   `gorm:"foreignKey:Nickname;references:Nickname" json:"health_history"`
	ActivityList  []Activity `gorm:"foreignKey:Nickname;references:Nickname" json:"activity_list"`
}

func (user *User) Create() (*User, error) {
	err := database.DB.Create(user).Error
	if err != nil {
		return &User{}, err
	}
	return user, nil
}

func (user *User) BeforeCreate(*gorm.DB) error {
	user.Nickname = html.EscapeString(strings.TrimSpace(user.Nickname))
	return nil
}

func Find(nickname string) (*User, error) {
	var user User
	err := database.DB.Where("nickname = ?", nickname).First(&user).Error
	if err != nil {
		return &User{}, err
	}
	return &user, nil
}

func (user *User) Update() (*User, error) {
	err := database.DB.Save(&user).Error
	if err != nil {
		return &User{}, err
	}
	return user, nil
}

func (user *User) Delete() error {
	err := database.DB.Delete(&user).Error
	if err != nil {
		return err
	}
	return nil
}
