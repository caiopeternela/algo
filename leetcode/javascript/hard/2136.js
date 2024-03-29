/* https://leetcode.com/problems/earliest-possible-day-of-full-bloom/submissions/877764882 */

/**
 * @param {number[]} plantTime
 * @param {number[]} growTime
 * @return {number}
 */
var earliestFullBloom = function(plantTime, growTime) {
  let time = [], totalPlantTime = 0, totalBloomTime = 0

  for (const i in plantTime) {
      time.push([plantTime[i], growTime[i]])
  }
  time.sort((x, y) => y[1] - x[1])

  for (const [plantTime, growTime] of time) {
      totalPlantTime += plantTime
      totalBloomTime = Math.max(totalBloomTime, totalPlantTime + growTime)
  }
  return totalBloomTime
}
