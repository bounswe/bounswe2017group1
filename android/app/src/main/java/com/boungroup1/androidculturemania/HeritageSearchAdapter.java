package com.boungroup1.androidculturemania;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by user on 03/12/2017.
 */

public class HeritageSearchAdapter extends RecyclerView.Adapter<HeritageSearchAdapter.MyViewHolder>{

    private ArrayList<JsonResponseSearchHeritage> heritageList;



    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView title, description, location, creator_username ;

        public MyViewHolder(View view) {
            super(view);
            title = (TextView) view.findViewById(R.id.heritage_search_title_text);
            description = (TextView) view.findViewById(R.id.heritage_search_description_text);
            location = (TextView) view.findViewById(R.id.heritage_search_location_text);
            creator_username = (TextView) view.findViewById(R.id.heritage_search_creator_username_text);
        }
    }


    public HeritageSearchAdapter(ArrayList<JsonResponseSearchHeritage> heritageList) {
        this.heritageList = heritageList;
    }

    @Override
    public HeritageSearchAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.heritage_search_view, parent, false);

        return new HeritageSearchAdapter.MyViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(HeritageSearchAdapter.MyViewHolder holder, int position) {

        final JsonResponseSearchHeritage heritageItem = heritageList.get(position);
        holder.title.setText(heritageItem.getTitle());
        holder.description.setText(heritageItem.getDescription());
        holder.location.setText(heritageItem.getLocation());
        holder.creator_username.setText("By " + heritageItem.getCreator_username());
    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }

}
