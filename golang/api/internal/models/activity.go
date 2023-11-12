package models

import "example/workout_api_golang/internal/database"

type Activity struct {
	Nickname string `gorm:"foreignKey:nickname;references:nickname" json:"nickname"`
	Activity string `gorm:"size:255;not null" json:"activity"`
	Duration uint   `gorm:"not null" json:"duration"`
	Kcal     uint   `gorm:"not null" json:"kcal"`
	Date     string `gorm:"not null" json:"date"`
}

func (activity *Activity) Create() (*Activity, error) {
	err := database.DB.Create(&activity).Error
	if err != nil {
		return &Activity{}, err
	}
	return activity, nil
}

func (activity *Activity) Find() (*Activity, error) {
	err := database.DB.Where("nickname = ?", activity.Nickname).First(&activity).Error
	if err != nil {
		return &Activity{}, err
	}
	return activity, nil
}

func (activity *Activity) Update() (*Activity, error) {
	err := database.DB.Save(&activity).Error
	if err != nil {
		return &Activity{}, err
	}
	return activity, nil
}

func (activity *Activity) Delete() error {
	err := database.DB.Delete(&activity).Error
	if err != nil {
		return err
	}
	return nil
}
