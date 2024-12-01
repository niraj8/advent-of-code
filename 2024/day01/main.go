package main

import (
	"io"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func MustAtoi(str string) int {
	i, err := strconv.Atoi(str)
	if err != nil {
		log.Print(err)
		log.Fatalln("failed to convert string to int")
	}
	return i
}

func main() {
	// input parsing
	stdin, err := io.ReadAll(os.Stdin)

	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(string(stdin), "\n")

	listA := make([]int, len(lines))
	listB := make([]int, len(lines))

	for i, line := range lines {
		locationIds := strings.Split(line, "   ")
		listA[i] = MustAtoi(locationIds[0])
		listB[i] = MustAtoi(locationIds[1])
	}
	slices.Sort(listA)
	slices.Sort(listB)
	calculateDistance(listA, listB)

}

func calculateDistance(listA []int, listB []int) {
	totalDistance := 0
	for i := range listA {
		distance := listA[i] - listB[i]
		if distance < 0 {
			totalDistance += -distance
		} else {
			totalDistance += distance
		}
	}
	log.Println("total distance:", totalDistance)
}
