package com.boungroup1.androidculturemania;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.View;

/**
 * Created by mehmetsefa on 03/12/2017.
 * Touch Listener for search list
 */

public class HeritageSearchRecyclerTouchListener implements RecyclerView.OnItemTouchListener {
    /**
     * ClickListener Interface
     */
    public interface ClickListener {
        void onClick(View view, int position);
        void onLongClick(View view, int position);
    }

    private GestureDetector gestureDetector;
    private HeritageSearchRecyclerTouchListener.ClickListener clickListener;

    /**
     * constructor for recycler view
     * @param context activity context
     * @param recyclerView recycler view
     * @param clickListener listener of click
     */
    public HeritageSearchRecyclerTouchListener(Context context, final RecyclerView recyclerView, final HeritageSearchRecyclerTouchListener.ClickListener clickListener) {
        this.clickListener = clickListener;
        gestureDetector = new GestureDetector(context, new GestureDetector.SimpleOnGestureListener() {
            @Override
            public boolean onSingleTapUp(MotionEvent e) {
                return true;
            }

            @Override
            public void onLongPress(MotionEvent e) {
                View child = recyclerView.findChildViewUnder(e.getX(), e.getY());
                if (child != null && clickListener != null) {
                    clickListener.onLongClick(child, recyclerView.getChildPosition(child));
                }
            }
        });
    }

    /**
     * touch event interceptor
     * @param rv recycler view
     * @param e motion event
     * @return false
     */
    @Override
    public boolean onInterceptTouchEvent(RecyclerView rv, MotionEvent e) {
        View child = rv.findChildViewUnder(e.getX(), e.getY());
        if (child != null && clickListener != null && gestureDetector.onTouchEvent(e)) {
            clickListener.onClick(child, rv.getChildPosition(child));
        }
        return false;
    }

    @Override
    public void onTouchEvent(RecyclerView rv, MotionEvent e) {
    }

    @Override
    public void onRequestDisallowInterceptTouchEvent(boolean disallowIntercept) {

    }

}

