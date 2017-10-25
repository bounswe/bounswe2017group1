package com.boungroup1.androidculturemania;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

/**
 * Created by user on 24/10/2017.
 */

public interface ApiInterface {

    @Headers( "Content-Type: application/json" )
    @POST("/api/users/signup")
    Call<JsonResponseSignUp> signUp(@Body SignUpBody signup);
    @Headers( "Content-Type: application/json" )
    @POST("/api/users/signin")
    Call<JsonResponseSignIn> signIn(@Body SignInBody signin);
//    @Headers( "Content-Type: application/json" )
//    @POST("/api/users/signin")
//    Call<JsonResponseSignIn> signIn(@Body SignInBody signin);
}
