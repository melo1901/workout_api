package model

type Health struct {
	Nickname       string  `gorm:"foreignKey:Nickname;references:Nickname" json:"nickname"`
	Blood_pressure string  `gorm:"size:255;not null" json:"blood_pressure"`
	Pulse          uint    `gorm:"not null" json:"pulse"`
	Weight         float32 `gorm:"not null" json:"weight"`
}
