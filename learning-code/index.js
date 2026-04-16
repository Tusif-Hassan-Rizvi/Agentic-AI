
const project = "gen Ai node";
import { Mistral } from "@mistralai/mistralai";

// console.log(project);

const apiKey =
  process.env.MISTRAL_API_KEY || "bBPVtggnVNzDcZuJGOki5ToFNdmNnmrm";
const model = "mistral-medium-latest";

const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.chat.complete({
  model: model,
  messages: [{ role: "user", content: "What is capital of india?" }],
});



console.log("this is model", chatResponse.choices[0]?.message);


