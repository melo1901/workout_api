package models

import "example/workout_api_golang/internal/database"

type Health struct {
	Nickname       string  `gorm:"foreignKey:Nickname;references:Nickname" json:"nickname"`
	Blood_pressure string  `gorm:"size:255;not null" json:"blood_pressure"`
	Pulse          uint    `gorm:"not null" json:"pulse"`
	Weight         float32 `gorm:"not null" json:"weight"`
}

func (health *Health) Create() (*Health, error) {
	err := database.DB.Create(&health).Error
	if err != nil {
		return &Health{}, err
	}
	return health, nil
}

func (health *Health) Find() (*Health, error) {
	err := database.DB.Where("nickname = ?", health.Nickname).First(&health).Error
	if err != nil {
		return &Health{}, err
	}
	return health, nil
}

func (health *Health) Update() (*Health, error) {
	err := database.DB.Save(&health).Error
	if err != nil {
		return &Health{}, err
	}
	return health, nil
}

func (health *Health) Delete() error {
	err := database.DB.Delete(&health).Error
	if err != nil {
		return err
	}
	return nil
}
