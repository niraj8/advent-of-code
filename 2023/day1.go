package main

import (
	"bufio"
	"os"
	"strconv"
)

func readInput() []string {
	reader := bufio.NewReader(os.Stdin)
	lines := make([]string, 0)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		lines = append(lines, line)
	}
	return lines
}

func calibrate(input []string) int {
	calibrationTotal := 0
	for _, line := range input {
		numbers := make([]string, 0)
		for _, c := range line {
			if c >= '0' && c <= '9' {
				numbers = append(numbers, string(c))
			}
		}
		calibrationValue, err := strconv.Atoi(numbers[0] + numbers[len(numbers)-1])
		if err != nil {
			panic(err.Error())
		}
		calibrationTotal += calibrationValue
	}
	return calibrationTotal
}


func main() {
	input := readInput()
	println(calibrate(input))
}
