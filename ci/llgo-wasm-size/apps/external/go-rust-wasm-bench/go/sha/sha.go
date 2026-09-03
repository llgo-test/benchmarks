package sha

import (
	"crypto/sha256"
	"fmt"
)

func Sum256Hex(data []byte) string {
	h := sha256.Sum256(data)
	return fmt.Sprintf("%x", h)
}
