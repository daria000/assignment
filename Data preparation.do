import delimited "C:/Users/Smirnova_Daria/Downloads/airbnb_hackney_workfile.csv"
display missing() /*0 missing values*/
keep usd_price_day f_property_type f_cancellation_policy p_host_response_rate n_review_scores_rating

*Keep only observations where cancellation policy is "strict"
keep if f_cancellation_policy == "strict"

*getting rid of na in observations
drop if !regexm(p_host_response_rate, "^[0-9.]+$")
drop if !regexm(n_review_scores_rating, "^[0-9.]+$")

// Create a binary variable (new_variable) based on existing_variable
egen biproperty = group(f_property_type)


