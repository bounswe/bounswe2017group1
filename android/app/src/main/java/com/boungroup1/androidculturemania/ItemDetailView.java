package com.boungroup1.androidculturemania;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.AppCompatImageView;
import android.text.method.ScrollingMovementMethod;
import android.view.MenuItem;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.TextView;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 22/11/2017.
 */

public class ItemDetailView extends AppCompatActivity {

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
        final TextView tag = (TextView) findViewById(R.id.tag);
        AppCompatImageView image = (AppCompatImageView) findViewById(R.id.detailimage);

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
