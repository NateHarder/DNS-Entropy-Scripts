import pandas as pd
import math



def entropy(string):
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy

def entropy_ideal(length):
    "Calculates the ideal Shannon entropy of a string with given length"

    prob = 1.0 / length

    return -1.0 * length * prob * math.log(prob) / math.log(2.0)

def main():
    # Read CSV file into DataFrame df
    df = pd.read_csv('names.csv', index_col=1)
    df.drop('label', inplace=True, axis=1)
    df["qlen"] = ""
    df["entropy"] = ""
    df["metric_entropy"] = ""
    df["alphabet_count"] = ""
    df["digit_count"] = ""
    df["is_Malicious"] = "1"

    i=0
    for q in df.iterrows():
        query = q[0]
        qlen = len(query)
        alphabet_count = 0 
        digit_count = 0
        for x in query:
            if x.isalpha():
                alphabet_count += 1
            if x.isdigit():
                digit_count += 1
        entropy_value = entropy(query)
        metric_entropy_value = entropy_ideal(len(query))
        df.iloc[i, 0] = str(qlen)
        df.iloc[i, 1] = str(entropy_value)
        df.iloc[i, 2] = str(metric_entropy_value)
        df.iloc[i, 3] = str(alphabet_count)
        df.iloc[i, 4] = str(digit_count)
        i += 1
    # Show dataframe
    print(df)
    df.to_csv(r'names2.csv')


if __name__ == "__main__":
    main()


