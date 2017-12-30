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
 * Created by mehmetsefa on 24/10/2017.
 * ApiInterface class contains the API end-points and all of the requests
 */

public interface ApiInterface {

    /**
     * SignUp API endpoint, connects us to the API
     * @param signup signup body for signup content
     * @return  response from API for signup
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/users/signup")
    Call<JsonResponseSignUp> signUp(@Body SignUpBody signup);

    /**
     * SignIn API endpoint, connects us to the API
     * @param signin content for signing in
     * @return response from API for signin
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/users/signin")
    Call<JsonResponseSignIn> signIn(@Body SignInBody signin);

    /**
     *  ItemCreate API endpoint, connects us to the API
     * @param itemcreate content for item creation
     * @param auth authorization token
     * @return response from API for item creation
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/items/")
    Call<JsonResponseItemCreate> itemCreate(@Body ItemCreateBody itemcreate, @Header("Authorization") String  auth);

    /**
     *  LogOut API endpoint, connects us to the API
     * @param auth authorization token
     * @return response for logout action
     */
    @GET("/api/users/signout")
    Call<JsonResponseSignOut> logOut(@Header("Authorization") String  auth);

    /**
     * List heritage that are taken from the API
     * @return list of heritage items
     */
    @GET("/api/items")
    Call<List<JsonResponseHeritage>> listHeritage();

    /**
     * Get Heritage Item Detail from API
     * @param id heritage item id
     * @param auth authorization token
     * @return heritage item detail response
     */
    @GET("/api/items/{id}")
    Call<JsonResponseItemDetail> getItem(@Path("id") int id, @Header("Authorization") String  auth);

    /**
     *  Voting Heritage Items
     * @param vote vote content to be sent to API
     * @param auth authorization token
     * @return response of the vote action
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/votes/")
    Call<JsonResponseVote> vote(@Body VoteBody vote, @Header("Authorization") String  auth);

    /**
     * Lists the Heritage Items that are ordered by ascending creation date
     * @return list of the new heritage items
     */
    @GET("/api/items/new")
    Call<List<JsonResponseHeritage>> listNewHeritage();

    /**
     *  Lists the top  popular heritage items
     * @return list of the top heritage irems
     */
    @GET("/api/items/top")
    Call<List<JsonResponseHeritage>> listTopHeritage();

    /**
     * Lists the trending heritage items
     * @return list of the trending heritage items
     */
    @GET("/api/items/trending")
    Call<List<JsonResponseHeritage>> listTrendingHeritage();

    /**
     * Gets comments of a heritage item
     * @param id heritage item id
     * @param auth authorization token
     * @return list of the comments of a heritage item
     */
    @GET("/api/items/{id}/comments")
    Call<List<JsonResponseComment>> getComments(@Path("id") int id, @Header("Authorization") String  auth);

    /**
     * Create a comment to a heritage item
     * @param itemcreate comment body
     * @param auth authorization token
     * @return comment response
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/comments/")
    Call<JsonResponseComment> commentCreate(@Body CommentBody itemcreate, @Header("Authorization") String  auth);

    /**
     * List the recommended heritage items to the user
     * @param auth authorization token
     * @return list of the recommended heritage items
     */
    @GET("/api/recommendation/user/")
    Call<List<JsonResponseHeritage>> listRecommendedHeritage(@Header("Authorization") String  auth);

    /**
     * Search heritage items
     * @param item heritage item that is searched
     * @param auth authorization token
     * @return list of the heritage items that are related to the search
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/search/")
    Call<List<JsonResponseSearchHeritage>> searchHeritage(@Body SearchHeritageBody item, @Header("Authorization") String  auth);

    /**
     * Upload Image for Heritage Items
     * @param authorization authorization token
     * @param image image body
     * @param type image type
     * @param heritage heritage item related to the image
     * @param creation_date date of creation
     * @param update_date date of update
     * @return response of the upload
     */
    @Multipart
    @POST("/api/medias")
    Call<JsonResponseMedia> uploadImage(@Header("Authorization") String authorization, @Part MultipartBody.Part image, @Part("type") String type, @Part("heritage") int heritage, @Part("creation_date") String creation_date, @Part("update_date") String update_date);

    /**
     * Upload video for heritage items
     * @param video video to be uploaded
     * @param auth authorization token
     * @return response of the upload
     */
    @Headers( "Content-Type: application/json" )
    @POST("/api/videos")
    Call<String> uploadVideo(@Body VideoBody video, @Header("Authorization") String  auth);

    /**
     * Delete a given vote
     * @param vote vote to be deleted
     * @param auth authorization token
     * @return response of the deletion
     */
    @Headers( "Content-Type: application/json" )
    @HTTP(method = "DELETE", path = "/api/votes", hasBody = true)
    Call<JsonResponseDeleteVote> deleteVote(@Body DeleteVoteBody vote,@Header("Authorization") String  auth);

    /**
     * Delete a Heritage Item
     * @param id heritage item id that is wanted to be deleted
     * @param auth authorization token
     * @return response of the deletion
     */
    @Headers( "Content-Type: application/json" )
    @HTTP(method = "DELETE", path = "/api/items/{id}", hasBody = false)
    Call<JsonResponseDeletePost> deletePost(@Path("id") int id, @Header("Authorization") String  auth);

    /**
     * Delete a comment
     * @param id comment id that is waned to be deleted
     * @param auth authorization token
     * @return response of the deletion
     */
    @Headers( "Content-Type: application/json" )
    @HTTP(method = "DELETE", path = "/api/comments/{id}", hasBody = false)
    Call<JsonResponseDeleteComment> deleteComment(@Path("id") int id, @Header("Authorization") String  auth);

}