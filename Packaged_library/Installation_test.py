try:
    import gethousevalue2.medianvalue as mv

    print("Library installation successful.")

    try:
        Train_data, Test_data = mv.ingest_data()
        prediction_model = mv.train(Train_data, 'Linear')
        rmse_score = mv.score(Train_data, Test_data, prediction_model)

        print('Library functionality tested succesfully.')

    except Exception as e:
        print('Library installation failed because of error:', e)

except Exception as e:
    print('Library installation failed because of error:', e)
