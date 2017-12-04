package com.boungroup1.androidculturemania;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by user on 29/11/2017.
 */

public class CommentAdapter extends RecyclerView.Adapter<CommentAdapter.MyViewHolder>{

    private ArrayList<JsonResponseComment> heritageList;



    public class MyViewHolder extends RecyclerView.ViewHolder {

        private TextView text, creator_username ;

        public MyViewHolder(View view) {
            super(view);
            text = (TextView) view.findViewById(R.id.comment_text);
            creator_username = (TextView) view.findViewById(R.id.comment_creator);
        }
    }


    public CommentAdapter(ArrayList<JsonResponseComment> heritageList) {
        this.heritageList = heritageList;
    }

    @Override
    public CommentAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.comment_view, parent, false);

        return new CommentAdapter.MyViewHolder(itemView);
    }


    @Override
    public void onBindViewHolder(CommentAdapter.MyViewHolder holder, int position) {

        final JsonResponseComment heritageItem = heritageList.get(position);
        holder.text.setText(heritageItem.getText());
        holder.creator_username.setText("By " + heritageItem.getCreator_username());
    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }

}
