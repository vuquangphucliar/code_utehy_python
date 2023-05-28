import pandas as pd
# Create data
df_sample = pd.DataFrame([["day1", "day2", "day1", "day2", "day1", "day2"],
                          ["A", "B", "A", "B", "C", "C"],
                          [100, 150, 200, 150, 100, 50],
                          [120, 160, 100, 180, 110, 80]]).T
# Add column name for the table
df_sample.columns = ["day_no", "class", "score1", "score2"]
# Tag the index for each rows
df_sample.index = [11, 12, 13, 14, 15, 16]
print(df_sample)
#    day_no class score1 score2
# 11   day1     A    100    120
# 12   day2     B    150    160
# 13   day1     A    200    100
# 14   day2     B    150    180
# 15   day1     C    100    110
# 16   day2     C     50     80