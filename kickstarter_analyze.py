import pandas as pd
import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv("Data/ks-projects-201801.csv")

# Get a quick visual on what the dataframe looks like
print(df.head(10))

# Choose a topic that may be interesting to study:
# Let's get a visual on successes and failures based on goal size
df['state_binary'] = df['state'].apply(lambda s: True if s == "successful" else False)
fig1, ax1 = plt.subplots()
ax1.scatter(df['usd_goal_real'], df['state_binary'])
ax1.set_xlabel('Goal (USD)')
ax1.set_ylabel('State (1=success, 0 = failure/cancelled)')
ax1.set_title('State vs Goal')
plt.show(block=False)

# This data doesn't show us too much, except that after a certain goal size pretty much
# nobody meets their goal. Let's do som calculations to get some better ideas
print()
print("Total number of successes = {:d}".format(np.sum(df['state_binary'])))
print("Total number of failures and cancelled = {:d}".format(np.sum(~df['state_binary'])))
print("This means that about {:.2f}% of Kickstarter campaigns in our data were successful".format((np.sum(df['state_binary'])/df.shape[0]) * 100))

# given our graph, this is somewhat surprising. It's obvious that almost all the successes are
# clustered in a certain goal range. Let's choose some bin ranges along the goal axis and plot
# a bar graph of the percentage of campaigns that were successful in each bin in order to see if anything
# stands out

# bin ranges: 0-10, 11-100, 101-1000, 1001-10000, 10001-100000, 100001-1000000

bin_ranges = ((0, 10), (11, 100), (101, 1000), (1001, 10000), (10001, 100000), (100001, 1000000))
def get_att_in_range(df, lower, upper):
    return df[df['usd_goal_real'].between(lower, upper, inclusive=True)].shape[0]

def get_succ_in_range(df, lower, upper):
    return sum(df[df['usd_goal_real'].between(lower, upper, inclusive=True)]['state_binary'])

def get_perc_suc_in_range(df, lower, upper):
    return get_succ_in_range(df, lower, upper)/get_att_in_range(df, lower, upper) * 100

fig2, ax2 = plt.subplots()
percent_succ_in_range = [get_perc_suc_in_range(df, br[0], br[1]) for br in bin_ranges]
b1, b2, b3, b4, b5, b6 = ax2.bar(np.arange(1,7), percent_succ_in_range, color='r', alpha=0.5)
x_labs = ["\$"+ str(br[0]) + " to \$" +str(br[1]) for br in bin_ranges]
ax2.set_xticks(np.arange(1,7))
ax2.set_xticklabels(x_labs, rotation=30, ha='right')
ax2.set_xlabel('Fundraising Goal')
ax2.set_ylabel('Percent Successful')
ax2.set_title('Percentage Successful vs Fundraising Goal')
plt.tight_layout()
plt.show(block=False)

# This is somewhat interesting, but may be misleading because it's not obvious
# how many kickstarter attempts were made in each range

# If we instead plot successful over total attempts in each range we get a
# better view of the data

def label_rects(ax, rects, labs):
    i = 0
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                labs[i], ha='center', va='bottom')
        i+=1

fig3, ax3 = plt.subplots()
att_in_range = np.array([get_att_in_range(df, br[0], br[1]) for br in bin_ranges])
succ_in_range = np.array([get_succ_in_range(df, br[0], br[1]) for br in bin_ranges])
ax3.bar(np.arange(1,7), att_in_range, color='b', alpha=0.5)
rects = ax3.bar(np.arange(1,7), succ_in_range, color='r', alpha=0.5)
x_labs = ["\$"+ str(br[0]) + " to \$" +str(br[1]) for br in bin_ranges]
bar_labs = ["{:.2f}".format(perc) + "%" for perc in percent_succ_in_range]
ax3.set_xticks(np.arange(1,7))
ax3.set_xticklabels(x_labs, rotation=30, ha='right')
ax3.set_xlabel('Fundraising Goal')
ax3.set_ylabel('Total Attempts and Successful Attempts')
ax3.set_title('Total Attempts and Successful Attempts vs Fundraising Goal')
label_rects(ax3, rects, bar_labs)
plt.tight_layout()
plt.show(block=False)

# From that we can see that most of the interesting data lies in kickstarter campaigns
# between $100 and $100,000

# Let's create a histogram to get a higher resolution image of what's going on in that range
def get_df_att_in_range(df, lower, upper):
    return df[df['usd_goal_real'].between(lower, upper, inclusive=True)]

def get_df_succ_in_range(df, lower, upper):
    temp = df[df['usd_goal_real'].between(lower, upper, inclusive=True)]
    return temp.loc[temp['state_binary'] == True]

df_succ = get_df_succ_in_range(df, 100, 100000)
df_att = get_df_att_in_range(df, 100, 100000)

fig4, ax4 = plt.subplots()
hist_bins = [x for x in range(1, 100001, 5000)]
n_att = ax4.hist(df_att['usd_goal_real'], bins=hist_bins, color='b', alpha=0.5)
n_succ = ax4.hist(df_succ['usd_goal_real'], bins=hist_bins, color='r', alpha=0.5)


bin_labs = ["{:.2f}".format(nn) for nn in n]


plt.show()
