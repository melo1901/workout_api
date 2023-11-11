package model

type Activity struct {
	Nickname string `gorm:"foreignKey:nickname;references:nickname" json:"nickname"`
	Activity string `gorm:"size:255;not null" json:"activity"`
	Duration uint   `gorm:"not null" json:"duration"`
	Kcal     uint   `gorm:"not null" json:"kcal"`
	Date     string `gorm:"not null" json:"date"`
}
