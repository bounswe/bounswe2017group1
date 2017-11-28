package com.boungroup1.androidculturemania;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.Headers;
import retrofit2.http.POST;
import retrofit2.http.Path;

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

    @Headers( "Content-Type: application/json" )
    @POST("/api/items/")
    Call<JsonResponseItemCreate> itemCreate(@Body ItemCreateBody itemcreate, @Header("Authorization") String  auth);

    @GET("/api/users/signout")
    Call<JsonResponseSignOut> logOut(@Header("Authorization") String  auth);

    @GET("/api/items")
    Call<List<JsonResponseHeritage>> listHeritage();

    @GET("/api/items/{id}")
    Call<JsonResponseItemDetail> getItem(@Path("id") int id, @Header("Authorization") String  auth);

    @Headers( "Content-Type: application/json" )
    @POST("/api/votes/")
    Call<JsonResponseVote> vote(@Body VoteBody vote, @Header("Authorization") String  auth);

    @GET("/api/items/new")
    Call<List<JsonResponseHeritage>> listNewHeritage();

    @GET("/api/items/top")
    Call<List<JsonResponseHeritage>> listTopHeritage();

    @GET("/api/items/trending")
    Call<List<JsonResponseHeritage>> listTrendingHeritage();


}