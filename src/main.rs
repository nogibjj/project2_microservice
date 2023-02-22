// build a summarization model and generate a summary using Tease

use rust_bert::pipelines::summarization::SummarizationModel;

// fn summary() {
//     // Load model
//     let model = SummarizationModel::new(Default::default()).unwrap();

//     // Define input
//     let input = [
// " A/B Testing Isn’t Always Legal or Ethical¶
// Those are all practical business constraints, but there are also ethical and legal constraints many people face.

// For example, if you’re at a social media company and want to study the effects of harassment on customer retention, you can’t randomly assign people to be harassed!

// And even if you think certain experiments are ok, you also have to be mindful of what the public will say. In 2012, Facebook ran an experiment in which they manipulated the emotional valence of posts they saw in their feeds, showing them either more happy posts or more sad posts. The goal was to see how moods spilled over from one user to another on the network.

// The experiment was legal, but when people found out they were having the moods toyed with at random, they were furious. Now some tech people would say that “everything we do is to try and manipulate consumer happiness, how is this any different? And maybe you even believe that (though I think that, at the very least, deliberately showing people sad things means you’re doing harm, which is a huge no-no in human experimentation). But it doesn’t really matter, because it cost Facebook a lot of good will.

// Similar issues happened with OKCupid when they published research on how they manipulated people’s dating profiles. That, honestly, was a pretty standard experiment, but when it comes to messing with people’s hearts… you have to be careful.

// Finally, A/B randomizations aren’t always legal. For example, suppose you’re working in Human Resources for a company that wants to improve retention of younger tech wokers, and you want to offer childcare subsidies to employees. If that workforce is unionized, you can’t offer a benefit to only some people within a specific class of employees due to union contracts.

// Going Beyond Testing for the Future¶
// Another limitation of A/B tests is that we usually use them to do small scale tests to motivate larger, future rollouts. But sometimes we want to just measure the effect of a single, large intervention.

// In many areas of business, it’s increasingly common to hire outside companies to do very complicated projects, like administering government programs or providing a service to employees. In these situations, companies have increasingly found that paying vendors based on inputs (hours worked, money spent) doesn’t actually encourage vendors to do a very good job, or to try to be efficient – if you’re being paid on the basis of what you spend, you will obviously you will not have an incentive to cut costs!

// In these situations, companies are increasingly turning to something called “at-risk contracting.” In these arrangements, the company doing the hiring offers to pay the vendor if they achieve a specific outcome. For example, a hospital might hire a company to reduce in-hospital infections and pay them based on reductions in infections, or a company may hire a vendor to minimize the downtime of their internal network, and pay them based on downtime. By tying compensation to the outcome that the hiring party actually cares about, the vendors well incentivized to do precisely what the hiring company wants them to do!

// But in these arrangements, it’s critical to both parties that there’s a good way to measure the effect of the vendor’s efforts or someone will get over or under paid. That’s not an average effect, that’s a specific effect, and something for which experiments are not well-suited.

// In these circumstances, it’s unfortunately the case that people often just measure outcomes before the vendor starts and compare them to outcomes when the vendor finishes. But if the outcome in question is subject to natural variation – such as seasonality – then we expect the outcome to vary whether the vendor does anything or not, and so you need a better causal design (e.g. difference-in-difference) to take those types of confounders into account.

// Don’t want to be limited¶
// Here’s another important thought: professionally, if you only know how to do A/B testing, you risk limiting your opportunities for upward advancement. Big companies are getting better and better at providing analysts with extremely user friendly A/B testing tools, which means doing A/B tests is getting easier and easier. Twitter, for example, has an internal tool called Duck, Duck, Goose that makes running an A/B test a relatively low-difficulty task. And while running a good A/B test is never easy (as we have discussed at length, even with A/B testing, the internal and external validity of our causal estimates will always be dependent on a wide range of assumptions), it is something that more and more people are learning to do well and which companies are learning to make easier. Thus, if all you know how to do are A/B tests, you may find it increasingly hard to differentiate yourself in the data science market.

// Again, this isn’t to say you shouldn’t learn to do A/B testing, just don’t only learn A/B testing.

// Not enough to be able to do it; you must be able to explain it¶
// One final reason it’s important to understand how to apply the logic of causal inference to observational data is that even if you only work with A/B data, it is almost inevitable that you will interact with other people in your company who want to use observational data. In these situations, it’s not enough that you understand the considerations that go into making causal inferences from observational data; you also need to be able to explain those to colleagues.",
//     ];

//     // Summarize text
//     let output = model.summarize(&input);

//     // Print summarized text
//     println!("{:?}", output);
// }

use tease::{Teaser, Input};
Teaser::default()
    .with_title("Summarizer".to_string())
    .with_description("This is for summarizing texts.".to_string())
    .with_inputs(vec![Input::default(); 2])
    .with_function(|inputs| {
        let input = inputs.iter().map(|i| i.text.as_str()).collect::<Vec<&str>>();
        let model = SummarizationModel::new(Default::default()).unwrap();
        let output = model.summarize(&input);
        output
    })
    .run();