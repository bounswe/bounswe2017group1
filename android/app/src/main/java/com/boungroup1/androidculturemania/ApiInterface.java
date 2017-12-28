package com.boungroup1.androidculturemania;

import java.util.List;

import okhttp3.MultipartBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.HTTP;
import retrofit2.http.Header;
import retrofit2.http.Headers;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
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

    @GET("/api/items/{id}/comments")
    Call<List<JsonResponseComment>> getComments(@Path("id") int id, @Header("Authorization") String  auth);

    @Headers( "Content-Type: application/json" )
    @POST("/api/comments/")
    Call<JsonResponseComment> commentCreate(@Body CommentBody itemcreate, @Header("Authorization") String  auth);

    @GET("/api/recommendation/user/")
    Call<List<JsonResponseHeritage>> listRecommendedHeritage(@Header("Authorization") String  auth);

    @Headers( "Content-Type: application/json" )
    @POST("/api/search/")
    Call<List<JsonResponseSearchHeritage>> searchHeritage(@Body SearchHeritageBody item, @Header("Authorization") String  auth);

    @Multipart
    @POST("/api/medias")
    Call<JsonResponseMedia> uploadImage(@Header("Authorization") String authorization, @Part MultipartBody.Part image, @Part("type") String type, @Part("heritage") int heritage, @Part("creation_date") String creation_date, @Part("update_date") String update_date);

    @Headers( "Content-Type: application/json" )
    @POST("/api/videos")
    Call<String> uploadVideo(@Body VideoBody video, @Header("Authorization") String  auth);

    @Headers( "Content-Type: application/json" )
    @HTTP(method = "DELETE", path = "/api/votes", hasBody = true)
    Call<JsonResponseDeleteVote> deleteVote(@Body DeleteVoteBody vote,@Header("Authorization") String  auth);

    @Headers( "Content-Type: application/json" )
    @HTTP(method = "DELETE", path = "/api/items/{id}", hasBody = false)
Call<JsonResponseDeletePost> deletePost(@Path("id") int id, @Header("Authorization") String  auth);

}