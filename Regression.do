* Convert string variable to numeric
gen num_rating = real(n_review_scores_rating)
gen num_price = real(usd_price_day)
gen num_responce = real(p_host_response_rate)

* Running ordinary least squares regressiuon stata
regress num_price num_rating num_responce

* make a graph
scatter num_price num_rating