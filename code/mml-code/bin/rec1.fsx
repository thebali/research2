#r @"mymedialite/MyMediaLite.dll"

open System

open MyMediaLite.IO
open MyMediaLite.RatingPrediction
open MyMediaLite.Eval
open MyMediaLite.Data

Environment.CurrentDirectory <- @"../../data/digitalmusic/ratings/"

(* load the data *)
let dataset = RatingData.Read "dm-ratings.csv"

let splitdata = RatingCrossValidationSplit(dataset, (uint32)10)

let traindata = splitdata.Train |> Seq.map(x:> IRatings)

let testdata = splitdata.Test

(* set up the recommender *)
let recommender = new UserItemBaseline(Ratings=traindata)
recommender.Train()

(* measure the accuracy on the test data set *)
let result = recommender.Evaluate(testdata)
Console.WriteLine(result)

(* make a prediction for a certain user and item *)
let prediction = recommender.Predict(1, 1)

Console.WriteLine(prediction)

