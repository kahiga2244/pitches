from flask import render_template
from app import app
from flask_login import login_required, current_user
from .forms import UpdateProfile, GeneralForm, GeneralReviewForm, SaleForm, SaleReviewForm, SeductionForm, SeductionReviewForm, MusicForm, MusicReviewForm, ProjectForm, ProjectReviewForm, InterviewForm, InterviewReviewForm, AdvertisementForm, AdvertisementReviewForm
from ..models import User, Interview, Advertisement, Project, Music, Sale, Seduction, General, ReviewAdvertisement, ReviewGeneral, ReviewInterview, ReviewMusic, ReviewProject, ReviewSale, ReviewSeduction, Upvote, Downvote

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the Pitches website'
    return render_template('index.html',title = title)

@main.route('/user/category/interviews')
@login_required
def interviews():
    title = 'Interview'
    posts = Interview.query.all()
    return render_template("inter.html", posts=posts, title=title)



@main.route('/user/interview/<int:id>', methods=['GET', 'POST'])
@login_required
def displayinterview(id):
    interview = Interview.query.get(id)
    form = InterviewReviewForm()
    if form.validate_on_submit():
        review = form.review.data
        new_interviewreview = ReviewInterview(
            review=review, interview_id=id, user=current_user)
        new_interviewreview.save_reviewinterview()

    review = ReviewInterview.query.filter_by(interview_id=id).all()
    return render_template('interviewpitch.html', interview=interview, review_form=form, review=review)