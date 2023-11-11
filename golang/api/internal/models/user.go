package model

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
