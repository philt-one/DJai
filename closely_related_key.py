# Closely Related Key
#
# In music, a closely related key (or "close key") is one sharing 
# many common tones with an original key, as opposed to a distantly 
# related key (or "distant key"). Given a major key tonic, 
# the related keys are:
#
#  - III: Supertonic, the relative minor of the subdominant
#  - III: Mediant, the relative minor of the dominant
#  - IV: Subdominant, one less sharp (or one more flat) around circle of fifths
#  - V: Dominant, one more sharp (or one fewer flat) around circle of fifths
#  - VI: Submediant or relative minor, different tonic, same key signature

def close_key(current_key):
        
    circle_fifth = {
        "major" : [
            "C", "G", "D",
            "A", "E", "B",
            "Gb", "Db", "Ab",
            "Eb", "Bb", "F" ], 
        "minor" : [
            "Am", "Em", "Bm",
            "Gbm", "Dbm", "G#m",
            "Ebm", "Bbm", "Fm",
            "Cm", "Gm", "Dm"]}
    
    if "m" in current_key:
        scale = circle_fifth["minor"]
        inv_scale = circle_fifth["major"]
                
    else:
        scale = circle_fifth["major"]
        inv_scale = circle_fifth["minor"]
        
    index_key = scale.index(current_key)
    submediant = inv_scale[index_key]
    subdominant = scale[(index_key - 1) % 12]
    dominant = scale[(index_key + 1) % 12]
        

    return [current_key, submediant, subdominant, dominant]
    