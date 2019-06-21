from scipy.interpolate import interp1d
import gunagala.sky as skies

class Spectrum:

    def __init__(self, wavelengths, fluxes):
        self.wavelengths = wavelengths
        self.fluxes = fluxes

    def sample(self, wave):
        wave = wave.to(u.AA)
        flux_units = self.fluxes.unit
        interpolated_object = interp1d(self.wavelengths.to(u.AA), self.fluxes)
        sampled_value = interpolated_object(wave)
        return(sampled_value*flux_units)

    def renorm(renorm_flux, units, filter_bandpass):
        pass


    def effective_stimulus(filter_bandpass):
        pass


    def spectral_density_equivalencies(units):
        specific_intensity = self.fluxes.to(units,
                equivalencies=u.equivalencies.spectral_density(wavelengths))
        return(specific_intensity)

class Zodical(Spectrum):

    def __init__(self):
        zodi_gunagala = skies.ZodiacalLight()
        zodi_flux = zodi_gunagala.photon_sfd
        zodi_waves = zodi_gunagala.waves
        self.fluxes = zodi_flux
        self.wavelengths = zodi_waves

class CIB(Spectrum):


class Earthshine(Spectrum):
       self.fluxes = zodi_flux
        self.wavelengths = zodi_waves

class CIB(Spectrum):


class Earthshine(Spectrum):
