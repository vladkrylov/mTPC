function tr = get_track(store_handle, event_id, track_id)
tr = NaN;
events = getappdata(store_handle, 'events');

% search in the newly added track
current_track = getappdata(store_handle, 'current_track');
if current_track.track_id == track_id && current_track.event_id == event_id
    tr = current_track;
end

% search in the rest of tracks stored in events structure
for iev=1:length(events)
    if events(iev).id == event_id
        for it=1:length(events(iev).selected_tracks)
            if events(iev).selected_tracks(it).track_id == track_id
                tr = it;
                return;
            end
        end
    end
end

end
