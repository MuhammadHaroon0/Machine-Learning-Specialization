const express = require("express");
const app = express();

const cors = require("cors");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());
const axios = require("axios");


app.post("/predict", async(req, res) => {
  try {
    const response = await axios.post("http://127.0.0.1:6000/predict", req.body, {
      headers: {
        "Content-Type": "application/json",
      },
    });

    const feats = response.data;
    console.log(feats);
    res.status(200).json(feats);
  } catch (error) {
    console.error("Error:", error.message);
    res.status(500).send("Internal Server Error");
  }

});
app.all("*", (req, res, next) => {
  console.log("No route found");
});

process.on("uncaughtException", (err) => {
  console.log(`${err.name} : ${err.message}`);
  console.log("Shutting down App");
  process.exit(1);
});

const server = app.listen(5000, () => {
  console.log("Server started at port " + 5000);
});

process.on("unhandledRejection", (err, promise) => {
  console.log(`${err.name} : ${err.message}`);
  console.log(`Atpromise: ${promise}`);
  console.log("Shutting down App");
  server.close(() => {
    process.exit(1);
  });
});
