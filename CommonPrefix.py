class Solution(object):
  def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      first = min(strs, key=len)
      strs.pop(strs.index(first))
      strs.insert(0, first)
      if first == "":
          return ""
      for i in range(1, len(strs)):
          for j in range(len(strs[i])):
              if strs[i] == "" or strs[i][0] != first[0]:
                  return ""
              try:
                  if strs[i][j] != first[j]:
                      first = first[0:j]
                      break
              except IndexError:
                  break

      return first