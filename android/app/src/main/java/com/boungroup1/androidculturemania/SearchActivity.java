package com.boungroup1.androidculturemania;

import android.app.SearchManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

/**
 * Created by user on 03/12/2017.
 */

public class SearchActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        Retrofit retrofit = ApiClient.getApiClient();
        ApiInterface apiInterface = retrofit.create(ApiInterface.class);

        // Get the intent, verify the action and get the query
        Intent intent = getIntent();
        String query = intent.getStringExtra(SearchManager.QUERY);

        final SharedPreferences sharedPref = getSharedPreferences("TOKENSHARED", Context.MODE_PRIVATE);
        final SharedPreferences.Editor editor = sharedPref.edit();
        final String  token = sharedPref.getString("TOKEN", null);

        Call<List<JsonResponseSearchHeritage>> call = apiInterface.searchHeritage(new SearchHeritageBody(query), "Token " + token);
        call.enqueue(new Callback<List<JsonResponseSearchHeritage>>() {
            @Override
            public void onResponse(Call<List<JsonResponseSearchHeritage>> call, Response<List<JsonResponseSearchHeritage>> response) {
                if (response.isSuccessful()) {
                    final ArrayList<JsonResponseSearchHeritage> heritageList = (ArrayList<JsonResponseSearchHeritage>) response.body();
                    setHeritageRecyclerView(heritageList);
                } else {
                    Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down" + response.code(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<List<JsonResponseSearchHeritage>> call, Throwable t) {
                Toast.makeText(getApplicationContext(), "Sorry for inconvince server is down", Toast.LENGTH_SHORT).show();
            }
        });



    }

    private void setHeritageRecyclerView(final ArrayList<JsonResponseSearchHeritage> heritageList){
        final RecyclerView heritageRecyclerView = (RecyclerView) findViewById(R.id.search_heritage_recycler_view);
        final HeritageSearchAdapter heritageAdapter = new HeritageSearchAdapter(heritageList);

        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(getApplicationContext());
        heritageRecyclerView.setLayoutManager(mLayoutManager);
        heritageRecyclerView.setItemAnimator(new DefaultItemAnimator());
        heritageRecyclerView.setAdapter(heritageAdapter);
        heritageAdapter.notifyDataSetChanged();
        heritageRecyclerView.addOnItemTouchListener(new HeritageSearchRecyclerTouchListener(getApplicationContext(), heritageRecyclerView, new HeritageSearchRecyclerTouchListener.ClickListener() {
            @Override
            public void onClick(View view, int position) {
                JsonResponseSearchHeritage heritage = heritageList.get(position);
                int heritageId= heritage.getId();
                Intent intent = new Intent(getApplicationContext(), ItemDetailView.class);
                intent.putExtra("heritageId",heritageId);
                finish();
                startActivity(intent);
            }

            @Override
            public void onLongClick(View view, int position) {
            }
        }));
    }
}
