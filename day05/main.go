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
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		log.Fatal("failed to read input", err)
	}
	input := strings.Split(string(stdin), "\n\n")
	rulesInput, updatesInput := input[0], input[1]
	// log.Print(rulesInput)
	// log.Print(updatesInput)

	rules := make([][]int, 0)
	updates := make([][]int, 0)
	for _, ruleInput := range strings.Split(rulesInput, "\n") {
		ruleInputArr := strings.Split(ruleInput, "|")
		rules = append(rules, []int{MustAtoi(ruleInputArr[0]), MustAtoi(ruleInputArr[1])})
	}

	for _, updateInput := range strings.Split(updatesInput, "\n") {
		update := make([]int, 0)
		for _, pageNum := range strings.Split(updateInput, ",") {
			update = append(update, MustAtoi(string(pageNum)))
		}
		updates = append(updates, update)
	}

	// log.Print(rules)
	// log.Print(updates)

	part1(rules, updates)
}

func part1(rules, updates [][]int) {
	result := 0
	rulesMap := make(map[int][]int, 0)
	for _, rule := range rules {
		rulesMap[rule[0]] = append(rulesMap[rule[0]], rule[1])
	}
	// log.Print(rulesMap)
	for _, update := range updates {
		if isUpdateCorrectlyOrdered(update, rulesMap) {
			result += update[len(update)/2]
		}
	}
	log.Print(result)
}

func isUpdateCorrectlyOrdered(update []int, rulesMap map[int][]int) bool {
	for i := 0; i < len(update); i++ {
		remainingPages := update[i+1:]
		// log.Print(len(remainingPages))
		pageNumX := update[i]
		// pagesThatShouldComeAfterX := make([]int, 0)
		if !containsAll(rulesMap[pageNumX], remainingPages) {
			return false
		}
	}
	return true
}

func containsAll(s []int, e []int) bool {
	for _, v := range e {
		if !slices.Contains(s, v) {
			return false
		}
	}
	return true
}
