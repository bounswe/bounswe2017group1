package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.text.method.ScrollingMovementMethod;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 22/11/2017.
 */

public class ItemDetailView extends AppCompatActivity {
    public boolean isUpVoted;
    public boolean isDownVoted;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.item_detail_view);

        final RelativeLayout layout = (RelativeLayout) findViewById(R.id.detail_view_relayout);
        layout.setVisibility(View.INVISIBLE);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();
        int heritageId = intent.getIntExtra("heritageId", -1);

        final TextView title = (TextView) findViewById(R.id.detailtitle);
        final TextView date = (TextView) findViewById(R.id.detaildate);
        final TextView location = (TextView) findViewById(R.id.detaillocation);
        final TextView name = (TextView) findViewById(R.id.detailname);
        final TextView description = (TextView) findViewById(R.id.detaildescription);
        final TextView voteCount = (TextView) findViewById(R.id.vote_count);
        final ImageButton upVote = (ImageButton) findViewById(R.id.up_vote_button);
        final ImageButton downVote = (ImageButton) findViewById(R.id.down_vote_button);
        final boolean isUpVoted;
        boolean isDownVoted;


        final TextView tag = (TextView) findViewById(R.id.tag);
        ImageView image = (ImageView) findViewById(R.id.detailimage);


        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);

        Call<JsonResponseItemDetail> call = apiInterface.getItem(heritageId, "Token " + token);
        call.enqueue(new Callback<JsonResponseItemDetail>() {
            @Override
            public void onResponse(Call<JsonResponseItemDetail> call, Response<JsonResponseItemDetail> response) {
                if(response.isSuccessful())
                {
                    if(response.body().isIs_upvoted())
                        upVote.setEnabled(false);
                    if(response.body().isIs_downvoted())
                        downVote.setEnabled(false);
                    voteCount.setText(Integer.toString(response.body().getUpvote_count()-response.body().getDownvote_count()));
                    //Log.d("RESPONSE", Integer.toString(response.body().getUpvote_count()));
                    String[] datestr = response.body().getEvent_date().toString().split("\\s+");
                    title.setText(response.body().getTitle());
                    date.setText(datestr[0] + "-"+ datestr[1] + "-" + datestr[2]);
                    location.setText(response.body().getLocation());
                    name.setText("By "+response.body().getCreator_username());
                    description.setText(response.body().getDescription());
                    for(TagResponse tags : response.body().getTags())
                    {
                        tag.append(tags.getName().toString());
                        tag.append(",");
                    }
                    layout.setVisibility(View.VISIBLE);
                }
            }

            @Override
            public void onFailure(Call<JsonResponseItemDetail> call, Throwable t) {

            }
        });

        description.setMovementMethod(new ScrollingMovementMethod());
        //TODO complete upvote function
        upVote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sendPostUpVote();
            }
        });

        downVote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sendPostDownVote();

            }
        });
    }

    public void sendPostUpVote(){
        Intent intent = getIntent();
        int heritageId = intent.getIntExtra("heritageId", -1);
        Retrofit retrofit = ApiClient.getApiClient();
        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseVote> call = apiInterface.vote(new VoteBody(true, heritageId),"Token " + token);
        call.enqueue(new Callback<JsonResponseVote>() {
            @Override
            public void onResponse(Call<JsonResponseVote> call, Response<JsonResponseVote> response) {

                if (response.isSuccessful()) {
                    Toast.makeText(getApplicationContext(), "SUCCESSFUL UPVOTE", Toast.LENGTH_SHORT).show();
                    finish();
                    startActivity(new Intent(getApplicationContext(), MainActivity.class));
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                    Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseVote> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });

    }
    public void sendPostDownVote(){
        Intent intent = getIntent();
        int heritageId = intent.getIntExtra("heritageId", -1);
        Retrofit retrofit = ApiClient.getApiClient();
        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final String  token = sharedPref.getString("TOKEN", null);
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);
        Call<JsonResponseVote> call = apiInterface.vote(new VoteBody(false, heritageId),"Token " + token);
        call.enqueue(new Callback<JsonResponseVote>() {
            @Override
            public void onResponse(Call<JsonResponseVote> call, Response<JsonResponseVote> response) {

                if (response.isSuccessful()) {
                    Toast.makeText(getApplicationContext(), "SUCCESSFUL DOWNVOTE", Toast.LENGTH_SHORT).show();
                    finish();
                    startActivity(new Intent(getApplicationContext(), MainActivity.class));
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                    Log.d("response", response.raw().body().toString());
                }

            }

            @Override
            public void onFailure(Call<JsonResponseVote> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "ERROR while posting", Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        finish();
        startActivity(new Intent(getApplicationContext(), MainActivity.class));
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            // Respond to the action bar's Up/Home button
            case android.R.id.home:
                finish();
                startActivity(new Intent(getApplicationContext(), MainActivity.class));
        }
        return super.onOptionsItemSelected(item);
    }
}
