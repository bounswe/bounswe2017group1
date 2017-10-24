package com.boungroup1.androidculturemania;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Headers;
import retrofit2.http.POST;
import retrofit2.http.Path;

/**
 * Created by user on 24/10/2017.
 */

public interface ApiInterface {

    @Headers( {"Content-Type: application/json" })
    @POST("/api/users/signup")
    Call<JsonResponseSignUp> signUp(@Body SignUpBody signup);
    Call<User> signIn();
}
