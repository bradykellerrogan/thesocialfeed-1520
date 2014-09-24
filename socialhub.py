import webapp2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

class MainPage(webapp2.RequestHandler):
  def get(self) :
    myHtml='''
<html> 

<head> 
	<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet"> 
	<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">

	<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

</head>


<body> 


</body>
<div id="main" class="container">  
	<div id="aggregate" class="col-md-12"> 
		<h2> Social Hub <small> Aggregate Social Media Feed </small></h2>

		<div class="social-posts"> 
			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small></h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-reddit-square"></i> Post Title </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-arrow-up"></i></a> <a href="#"><i class="fa fa-arrow-down"></i></a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>

		</div>
	</div>

	<div id="facebook" class="col-md-6"> 
		<h2> Facebook </h2>

		<div class="social-posts"> 
			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-facebook-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-thumbs-o-up"></i> Like </a>
					</div>			
				</div>
			</div>
		</div>
	</div>

	<div id="twitter" class="col-md-6"> 
		<h2> Twitter </h2>

		<div class="social-posts"> 
			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>


			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>


			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>


			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-twitter-square"></i> John Doe <small> Posted: 9/21/2014 2:09 PM </small> </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-star-o"></i> Favorite </a>
					</div>			
				</div>
			</div>

		</div>
	</div>

	<div id="reddit" class="col-md-6"> 
		<h2> Reddit </h2>

		<div class="social-posts"> 
			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-reddit-square"></i> Post Title </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-arrow-up"></i></a> <a href="#"><i class="fa fa-arrow-down"></i></a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-reddit-square"></i> Post Title </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-arrow-up"></i></a> <a href="#"><i class="fa fa-arrow-down"></i></a>
					</div>			
				</div>
			</div>

			<div class="media">
				<a class="pull-left" href="#">
				<img class="media-object hidden-xs" src="http://placehold.it/80x80" alt="profile-img">
				</a>
				<div class="media-body">
				<h4 class="media-heading"><i class="fa fa-reddit-square"></i> Post Title </h4>
					<p> Biodiesel kitsch meggings keffiyeh, keytar lomo tote bag chillwave. Wolf ugh synth, authentic Wes Anderson you probably haven't heard of them kale chips. Messenger bag occupy American Apparel, vegan mlkshk shabby chic fanny pack small batch next level banjo Godard synth Schlitz. McSweeney's roof party sriracha typewriter. </p>
					<div> 
						<a href="#"><i class="fa fa-arrow-up"></i></a> <a href="#"><i class="fa fa-arrow-down"></i></a>
					</div>			
				</div>
			</div>
		</div>
	</div>
</div>

</html>
'''
    self.response.out.write(myHtml)
   
 
app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)

app.run()