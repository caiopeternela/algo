/* https://leetcode.com/problems/reducing-dishes/ */


/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
  let result = 0
  satisfaction.sort((x,y)=>x-y)
  while(satisfaction.length > 0){
      let sum = 0
      for(let i in satisfaction){
          sum = sum + (satisfaction[i] * (Number.parseInt(i)+1))
      }
      if (sum > result)
          result = sum
      satisfaction.shift()
  }
  return result
}
