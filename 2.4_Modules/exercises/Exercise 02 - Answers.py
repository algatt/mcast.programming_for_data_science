import DataScienceBasics as dsp

def main():
    data = dsp.load_data('data.txt')
    new_data = dsp.filter_data(data, lambda x:x['score']!=100)
    new_data = dsp.transform_data(data, 'score', lambda x:x-5)
    stats = dsp.describe_data(new_data, 'score')

    print(f"Unique Players: {dsp.get_uniques(new_data, 'name')}")
    print(f"Score Mean: {stats[0]}\nScore Median: {stats[1]}")
    print (f"Players By Age\n{dsp.aggregate_data(new_data,'age')}")

if __name__ == "__main__":
    main()


