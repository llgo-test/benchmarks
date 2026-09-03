package jsonrt

import (
	"encoding/json"
	"sort"
)

type User struct {
	ID    int     `json:"id"`
	Name  string  `json:"name"`
	Email string  `json:"email"`
	Age   int     `json:"age"`
	Score float64 `json:"score"`
}

func Process(input []byte) ([]byte, error) {
	var users []User
	if err := json.Unmarshal(input, &users); err != nil {
		return nil, err
	}

	var filtered []User
	for _, u := range users {
		if u.Age >= 18 {
			filtered = append(filtered, u)
		}
	}

	sort.Slice(filtered, func(i, j int) bool {
		if filtered[i].Score != filtered[j].Score {
			return filtered[i].Score > filtered[j].Score
		}
		return filtered[i].ID < filtered[j].ID
	})

	return json.Marshal(filtered)
}
